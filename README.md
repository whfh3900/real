# real

>2023년 창업도약패키지 Real? 프로젝트. <br>
본 프로젝트에서는 django를 이용하여 Real?의 rest_framework 벡앤드를 구현하였습니다.<br>
API 양식에 맞게 request를 보내면 해당 거래가 특이거래 인지 아닌지 판단하여 결과를 respone 해줍니다.


![nicreal](./png/image.png)<br>


## 사용자 거래유형 보기(GET)
|URL|Request Body(Example)|STATE|Response Body(Example)|
|------|---|---|---|
|/api/{UID}||200|{"result": {"uid": "{UID}","c0": 19, ... "c12": 61,"note": ""},"state": 200,"error": null}|
|/api/{UID}||404|{"result": null,"state": 404,"error": "No UID matches the given query."}|<br>


## 사용자 거래유형 생성 및 특이거래 알림(POST)
|URL|Request Body(Example)|STATE|Response Body(Example)|
|------|---|---|---|
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|201|{"result": false,"state": 201,"error": null}|
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|400|{"result": null,"error": {"bas_ym": ["A valid integer is required."]},"state": 400}|<br>
|/api/{UID}|{"bas_ym":202203,"age_dc":"60","gender":1,"bas_dt":20,"tran_md":"입금","ats_kdcd_tl":"펌뱅킹 입금이체","dps_trm_am":8,"text_1":"소득"}|404|{"result": null,"state": 404,"error": "No UID matches the given query."},"state": 404}|<br>


## 정보

최승언 – [@velog](https://velog.io/@csu5216) – csu5216@gmail.com
