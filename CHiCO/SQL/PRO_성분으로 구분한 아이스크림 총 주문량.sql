다음은 아이스크림 가게의 상반기 주문 정보를 담은 FIRST_HALF 테이블과 아이스크림 성분에 대한 정보를 담은 ICECREAM_INFO 테이블입니다. FIRST_HALF 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR, TOTAL_ORDER 는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다. FIRST_HALF 테이블의 기본 키는 FLAVOR입니다.

NAME	TYPE	NULLABLE
SHIPMENT_ID	INT(N)	FALSE
FLAVOR	VARCHAR(N)	FALSE
TOTAL_ORDER	INT(N)	FALSE
ICECREAM_INFO 테이블 구조는 다음과 같으며, FLAVOR, INGREDITENT_TYPE 은 각각 아이스크림 맛, 아이스크림의 성분 타입을 나타냅니다. INGREDIENT_TYPE에는 아이스크림의 주 성분이 설탕이면 sugar_based라고 입력되고, 아이스크림의 주 성분이 과일이면 fruit_based라고 입력됩니다. ICECREAM_INFO의 기본 키는 FLAVOR입니다. ICECREAM_INFO테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키입니다.

NAME	TYPE	NULLABLE
FLAVOR	VARCHAR(N)	FALSE
INGREDIENT_TYPE	VARCHAR(N)	FALSE
# 문제
상반기 동안 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림의 총주문량을 총주문량이 작은 순서대로 조회하는 SQL 문을 작성해주세요. 이때 총주문량을 나타내는 컬럼명은 TOTAL_ORDER로 지정해주세요.


# 정답

SELECT B.INGREDIENT_TYPE, SUM(TOTAL_ORDER)
FROM FIRST_HALF A JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER 

# 이문제를 WHERE로 풀면 카르테시안 곱 사용되어 비효율적임

# JOIN 유형 
INNER JOIN: 두 테이블에서 일치하는 데이터만 필요할 때 사용.
LEFT JOIN: 왼쪽 테이블의 모든 데이터를 포함하고, 오른쪽 테이블의 관련 데이터를 추가하고 싶을 때 사용.
RIGHT JOIN: 오른쪽 테이블의 모든 데이터를 포함하고, 왼쪽 테이블의 관련 데이터를 추가하고 싶을 때 사용.
FULL JOIN: 두 테이블의 모든 데이터를 포함하고, 일치하지 않는 데이터도 모두 포함하고 싶을 때 사용 (MySQL에서는 UNION으로 대체).

INNER JOIN은 두 테이블 간의 공통된 데이터를 결합할 때 가장 많이 사용되며, 다른 유형의 JOIN은 특정 요구사항에 따라 선택