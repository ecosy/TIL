# REST API Using PostgreSQL
## 1. 프로젝트 소개
* golang을 사용해서 간단한 CRUD 기능의 REST API를 개발한다.
* Middleware - PostgreSQL을 사용한다.
---

## 2. 사용 데이터
* car 마다 고유한 key 값을 VIN (Vehicle Identification Number) 라고 지칭한다.
* VIN은 UUID의 형태를 갖는다. (32자리 16진수, 8-4-4-4-12)
```bash
(example) UUID : 550e8400-e29b-41d4-a716-446655440000
```
* 차량 관련 service 는 각각 고유한 service id(UUID 형태)를 갖는다.
* service id 와 VIN은 하나의 car id (UUID 형태)를 갖는다.

```bash
Charging Service id : c60cf43a-a076-45c4-b58f-86e75960ce24
Charging Service Secret : CharingSecret
(base64 encoded) Service Secret : Q2hhcmluZ1NlY3JldA==


Sharing Service id : 5cd4cd3a-c78f-11eb-b8bc-0242ac130003
Sharing Service Secret : SharingSecret
(base64 encoded) Service Secret : U2hhcmluZ1NlY3JldA==

K8 Car ID : fe6ccaa8-c78f-11eb-b8bc-0242ac130003
Sorento Car ID : 4a181c0a-c790-11eb-b8bc-0242ac130003
```

|Service Type|Service ID|Car Type|VIN|Car ID|
|:---:|:---:|:---:|:---:|:---:|
|Charging|c60cf43a-a076-45c4-b58f-86e75960ce24|K8|fe6ccaa8-c78f-11eb-b8bc-0242ac130003|0342296a-c790-11eb-b8bc-0242ac130003
|Sharing|5cd4cd3a-c78f-11eb-b8bc-0242ac130003|K8|fe6ccaa8-c78f-11eb-b8bc-0242ac130003|2623bd36-c790-11eb-b8bc-0242ac130003
|Charging|c60cf43a-a076-45c4-b58f-86e75960ce24|Sorento|4a181c0a-c790-11eb-b8bc-0242ac130003|57ccedb2-c790-11eb-b8bc-0242ac130003
|Sharing|5cd4cd3a-c78f-11eb-b8bc-0242ac130003|Sorento|4a181c0a-c790-11eb-b8bc-0242ac130003|63dda4ca-c790-11eb-b8bc-0242ac130003

---
## 3. API 명세서
* URI : /api/v1/profile/car/{car_id}/vin
* 이때 Service id는 api header의 basic token 값으로 받는다.

3.1 GET
* {car_id}에 대한 VIN 값을 리턴한다.

3.2 POST
* {car_id}에 대한 VIN 값을 입력받아 저장한다.

3.3 PUT
* {car_id}에 대한 VIN 값을 입력받아 기존 값을 수정한다.

3.4 DELETE
* {car_id}에 대한 VIN 값을 삭제한다.

---
## 4. Database - ERD
4.1 service table
* column : service id(PK), service name, service secret

4.2 car table
* column : VIN (PK), car type

4.3 map_service_car table
* column : car id (PK), service id (FK), VIN (FK)

---
