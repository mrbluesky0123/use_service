from point_use.models import *
from datetime import datetime

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

    # 입력값(null) 검증
    for data in request:
        if data is None:
            response['ans_cd'] = '1111'
            response['ans_msg'] = 'Invalid input'
            return response

    # 카드 검증
    crd_sts = Card.objects.get_card_status(data['crd_no'])
    if crd_sts != 'A':
        response['ans_cd'] = '1112'
        response['ans_msg'] = 'Invalid card'
        return response
    
    # 회원 ID get
    mbr_id = Card.objects.get_mbr_id_by_crd_no(data['crd_no'])

    # 회원 검증
    mbr_sts = Member.objects.get_member_status(mbr_id)
    if mbr_sts != 'A':
        response['ans_cd'] = '1113'
        response['ans_msg'] = 'Invalid member'
        return response
    
    # 가맹점 검증
    mcht_sts = Merchant.objects.get_merchant_status(data['mcht_no'])
    if mcht_sts != 'A':
        response['ans_cd'] = '1114'
        response['ans_msg'] = 'Invalid merchant'
        return response

    # 포인트 검증
    point = Point.objects.get_point(mbr_id)
    if point < data['deal_amt']:
        response['ans_cd'] = '1115'
        response['ans_msg'] = 'Point insufficient'
        return response

    # 포인트 사용(차감)
    remain_point = point - data['deal_amt']

    # 포인트 업데이트
    Point.objects.update_point(mbr_id, remain_point)

    # 응답값 반환
    response['ans_cd'] = '0000'
    response['ans_msg'] = 'OK'
    response['aprv_dy'] = datetime.today().strftime('%Y%m%d')
    response['aprv_tm'] = datetime.today().strftime('%H%M%S')
    response['apvr_no'] = '123456789'
    response['rmn_pnt'] = remain_point
    return response