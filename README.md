# real

>2023년 창업도약패키지 Real? 프로젝트. <br>
본 프로젝트에서는 django를 이용하여 Real?의 rest_framework 벡앤드를 구현하였습니다.<br>
API 양식에 맞게 request를 보내면 해당 거래가 특이거래 인지 아닌지 판단하여 결과를 respone 해줍니다.


![nicreal](./png/image.png)<br>


## 사용자 거래유형 및 거래이력 보기(GET) - update 2023-03-13
|URL|Request Body(Example)| STATE                                                                                             |Response Body(Example)|
|------|---|---------------------------------------------------------------------------------------------------|---|
|/api/{UID}||200| {"result": "userinfo":{"uid": "{UID}","c0": ...},"transaction:{...}" ,"state": 200,"error": null} |
|/api/{UID}||404| {"result": null,"state": 404,"error": "No UID matches the given query."}                          |<br>


## 사용자 거래유형 생성 및 특이거래 알림(POST)
|URL|Request Body(Example)|STATE|Response Body(Example)|
|------|---|---|---|
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|201|{"result": false,"state": 201,"error": null}|
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|400|{"result": null,"error": {"bas_ym": ["A valid integer is required."]},"state": 400}|<br>
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|404|{"result": null,"state": 404,"error": "No UID matches the given query."},"state": 404}|<br>


## 업데이트
- 2023-03-13(1): 사용자 거래유형(GET)에서 거래이력 보는 것도 포함.
- 2023-03-13(2): prefetch_related를 이용하여 UserInfo의 uid를 역참조하는 Transaction 데이터를 찾도록 함.
- 2023-03-13(3): 역참조하여 찾은 Transaction 데이터를 PageNumberPagination 기능을 사용하여 페이지별로 나눠서 보여지도록 함.

## 정보

최승언 – [@velog](https://velog.io/@csu5216) – csu5216@gmail.com
