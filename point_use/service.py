from point_use.models import *
from datetime import datetime
import json
import urllib

''' 사용 서비스 구현 '''
''' 2019. 02. 08 '''
def point_use(request):
    # request: dict
    # response: dict
    response = {
        'ans_cd': '',
        'ans_msg': '',
        'aprv_dy': '',
        'aprv_tm': '',
        'aprv_no': '',
        'rmn_pnt': '',
        'rep_aprv_no': '',
    }
    print('###########' + str(type(request)))
    # 입력값(null) 검증
    for data in request:
        if data is None:
            response['ans_cd'] = '1111'
            response['ans_msg'] = 'Invalid input'
            return response

    # 카드 검증
    crd_sts = Card.objects.get_card_status(request['crd_no'])
    if crd_sts == None:
        response['ans_cd'] = '2011'
        response['ans_msg'] = 'No card registered'
        return response
    elif crd_sts != 'A':
        response['ans_cd'] = '1112'
        response['ans_msg'] = 'Invalid card'
        return response
    
    # 회원 ID get
    mbr_id = Card.objects.get_mbr_id_by_crd_no(request['crd_no'])

    # 회원 검증
    mbr_sts = Member.objects.get_member_status(mbr_id)
    if mbr_sts == None:
        response['ans_cd'] = '2012'
        response['ans_msg'] = 'No member exists'
        return response
    elif mbr_sts != 'A':
        response['ans_cd'] = '1113'
        response['ans_msg'] = 'Invalid member'
        return response
    
    # 가맹점 검증
    mcht_sts = Merchant.objects.get_merchant_status(request['mcht_no'])
    if mcht_sts == None:
        response['ans_cd'] = '2013'
        response['ans_msg'] = 'No merchant exists'
        return response
    elif mcht_sts != 'A':
        response['ans_cd'] = '1114'
        response['ans_msg'] = 'Invalid merchant'
        return response

    # 포인트 검증
    point = Point.objects.get_point(mbr_id)
    if point < int(request['deal_amt']):
        response['ans_cd'] = '1115'
        response['ans_msg'] = 'Point insufficient'
        return response

    # 포인트 사용(차감)
    remain_point = point - int(request['deal_amt'])

    # 포인트 업데이트
    if Point.objects.update_point(mbr_id, remain_point) < 0:
        response['ans_cd'] = '2014'
        response['ans_msg'] = 'Something wrong'
        return response

    # 승인정보 받아오기
    mcht_fg = Merchant.objects.get_merchant_flag(request['mcht_no'])
    aprv_info = _get_approve_info(request['mcht_no'], mcht_fg)
    
    # 예외처리

    # 응답값 반환
    response['ans_cd'] = '0000'
    response['ans_msg'] = 'OK'
    response['aprv_dy'] = aprv_info['aprv_dy']
    response['aprv_tm'] = aprv_info['aprv_tm']
    response['rep_aprv_no'] = aprv_info['rep_aprv_no']
    response['rmn_pnt'] = remain_point
    return response

''' 외부 API 연동 '''
''' 2019. 02. 08 '''
def _get_approve_info(mcht_no, mcht_fg):
    req_url = 'http://198.13.47.188:9090/spring5mvc_war/aprv_no'
    header = {'Content-Type': 'application/json'}
    body = {
	    "svc_modu_id": "APPROVE",
	    "telgrm_fg": "ON",
	    "onoff_mcht_fg": mcht_fg,
	    "mbrsh_pgm_id": "A",
	    "mcht_no": mcht_no
    }
    # data = bytes(urllib.parse.urlencode(body).encode())
    request = urllib.request.Request(url=req_url, data=json.dumps(body).encode('utf-8'), headers=header)
    response = urllib.request.urlopen(request).read().decode('utf-8')
    result = json.loads(response)
    print(result) 
    return result