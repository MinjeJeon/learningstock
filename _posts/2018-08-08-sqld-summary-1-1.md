---
title: SQL 전문가 / 개발자 요약 - 1과목 1장 데이터 모델링의 이해
date: 2018-08-08 23:00 +0900
categories:
- SQL
layout: post
published: true
---

## 제 1절 데이터 모델의 이해

### 1. 모델링의 이해

* 모델링의 정의
    * 다양한 현상에 대해 일정한 표기법에 의해 표현해 놓은 모형(모델)을 만드는 것
    * 다양한 정의
        * 가설적 또는 일정 양식에 맞춘 표현
        * 예비표현으로 최종대상이 구축되도록 하는 계획
        * 복잡한 '현실세계'를 단순화하여 표현하는 것
        * 사물 또는 사건에 관한 양상이나 관점을 연관된 사람이나 그룹을 위하여 명확하게 하는 것
        * 현실 세계의 추상화된 변형
* 모델링의 특징
    * 추상화: 현실세계를 일정한 형식(표기법)에 맞추어 표현.
    * 단순화: 복잡한 현실세계를 약속된 규약에 의해 제한된 표기법이나 언어로 표현. 쉽게 이해할 수 있도록 하는 개념
    * 명확화: 누구나 이해하기 쉽게 하기 위해 애매모호함을 제거, 정확하게 현상을 기술
* 모델링의 3가지 관점
    * 데이터관점: 업무가 어떤 데이터와 관련이 있는지, 데이터간의 관계는 무엇인지(What, Data)
    * 프로세스관점: 업무가 실제 하고 있는 일은 무엇인지, 무엇을 해야 하는지(How, Process)
    * 데이터와 프로세스의 상관관점: 업무가 처리하는 일의 방법에 따라 데이터는 어떻게 영향을 받고 있는지(Interaction)
    * 여기서는 데이터 관점만 봄

### 2. 데이터 모델의 기본 개념의 이해

* 데이터 모델링의 정의
    * 정의
        * 정보시스템을 구축하기 위한 데이터관점의 업무 분석 기법
        * 현실세계의 데이터(what)에 대해 약속된 표기법에 의해 표현하는 과정
        * 데이터베이스를 구축하기 위한 분석/설계의 과정
    * 실무적으로는 업무에서 필요로 하는 데이터를 시스템 구축 방법론에 의해 분석하고 설계하여 정보시스템을 구축하는 과정
    * 목적
        * 업무정보를 구성하는 기초가 되는 정보들을 일정한 표기법에 의해 표현
        * 분석된 모델을 가지고 실제 데이터베이스를 생성하여 개발 및 데이터관리에 사용
        * 모델링 자체로도 업무를 설명하고 분석하는 의미
* 데이터 모델이 제공하는 기능
    * 시스템의 구조와 행동 명세화
    * 시스템 구축하는 구조화된 틀 제공
    * 시스템 구축 과정에서 결정한 것을 문서화
    * 다양한 영역에 집중하기 위해 다른 영역의 세부사항은 숨기는 다양한 관점 제공
    * 특정 목표에 따라 구체화된 상세 수준의 표현방법 제공

### 3. 데이터 모델링의 중요성 및 유의점

* 파급효과
    * 애플리케이션 완성 단계에서 데이터가 변경되면 많은 영향 분석 필요. 데이터 설계가 가장 중요
* 복잡한 정보 요구사항의 간결한 표현(Concsiseness)
    * 건축물로 비유하자면 설계 도면, 여러 사람이 공유하면서 일사불란하게 움직일 수 있게 함
    * 정보 요구사항이 명확하고 간결하게 표현되어야 함
* 데이터 품질
    * 정확성이 떨어지는 데이터는 해당 데이터로 얻을 수 있는 비즈니스 기회 상실
* 유의점
    * 중복
    * 비유연성: 사소한 업무변화에 데이터 구조가 변하면 안됨
    * 비일관성: 하나의 데이터를 고칠 때 다른 데이터와 모순 발생

### 4. 데이터 모델링의 3단계 진행

* 개념적: 추상화 수준 높고 업무중심적, 포괄적 수준, EA(Enterprise Architecture)수립 시
    * 사용자, 시스템 개발자가 데이터 요구 사항을 발견하는 것을 지원
    * 현 시스템이 어떻게 변형되어야 하는지 이해하는데 유용
* 논리적: 시스템으로 구축하고자 하는 업무에 대해 Key, 속성, 관계등을 정확하게 표현
    * 비즈니스 정보의 논리적인 구조와 규칙을 명확하게 표현
    * 데이터 모델링 중 가장 핵심
    * 정규화: 식별자 확정, M:M관계 해소 참조 무결성 규칙 정의
* 물리적: 실제로 데이터베이스에 이식할 수 있도록 성능, 저장등 물리적인 성격 고려
    * 데이터가 물리적으로 컴퓨터에 어떻게 저장될 것인가 결정
    * 테이블, 컬럼으로 표현되는 물리적인 저장구조, 저장장치, 접근방법 결정

### 5. 프로젝트 생명주기에서 데이터 모델링

* 폭포수 기반 : 분석(논리적 데이터 모델링)과 설계(물리적 데이터 모델링)단계로 구분되어 명확하게 정의
* 나선형 모델 : 분석, 설계 둘다 하는데 분석 단계에서 논리적 데이터 모델이 더 많이 수행
  
### 6. 데이터 모델링에서의 데이터독립성의 이해

* 데이터독립성의 필요성
    * 데이터가 응용(Application)에 종속되지 않음
    * 유지보수 비용 절감, 데이터복잡도↓, 데이터중복성↓, 바뀌는 요구사항에 대응능력 강화
    * 효과: 각 View의 독립성 유지, 단계별 Schema에 따라 DDL, DML이 다름
* 데이터베이스의 3단계 구조 / 데이터독립성 요소
    * 외부단계: 사용자와 가까운 단계, 개개인(Application/User)이 보는 자료에 대한 관점
    * 개념단계: 하나의 개념적 스키마로 사용자 관점을 통합. 통합한 조직 전체의 DB
    * 내부스키마: DB가 물리적으로 저장된 형식
* 두 영역의 데이터독립성
    * 논리적 독립성: 개념 스키마가 바뀌어도 외부 스키마에 영향없음
    * 물리적 독립성: 내부스키마가 변경되어도 외부스키마는 영향 받지 않음
* 사상(Mapping)
    * 외부적/개념적 사상(논리적 사상)
        * 외부적 뷰와 개념적 뷰의 상호 관련성
    * 개념적/내부적 사상(물리적 사상)
        * 개념적 뷰와 저장된 데이터베이스의 상호관련성
    * 데이터 독립성을 보장하려면 하나가 바뀔 때 각 단계를 연결시켜주는 사상 스크립트(DDL)을 DBA가 바꿔주어야 함.
    * DBA의 적절한 작업으로 독립성이 보장됨
  
### 7. 데이터 모델링의 중요한 세 가지 개념

* 데이터 모델링의 세 가지 요소

    | 개념                                          | 복수/집합개념<br>타입/클래스 | 개별/단수개념<br>어커런스/인스턴스 |
    |:----------------------------------------------|:-----------------------------|:-----------------------------------|
    | 업무가 관여하는 어떤 것(Thing)                | 엔터티                       | 인스턴스/어커런스(Occurrence)      |
    | 업무가 관여하는 어떤 것의 관계(Relationships) | 관계                         | 페어링                             |
    | 어떤 것이 가지는 성격(Attributes)             | 속성                         | 속성값                             |

### 8. 데이터 모델링의 이해관계자

* 이해관계자의 데이터 모델링 중요성 인식
    * 데이터에 기반한, 데이터가 중심이 있는 정보시스템
    * 핵심인 데이터베이스 설계가 잘못된 경우 미치는 영향은 모든 프로그램, 모든 데이터, 모든 트랜잭션에 영향
* 데이터 모델링의 이해관계자
    * 정보시스템을 구축하는 모든 사람(코딩만 하는 사람 포함) / 모든 IT기술자: 모델링에 대해 정확히 이해
    * 비 IT 기술자 / 업무 담당자: 데이터 모델링의 대한 개념 및 세부사항에 대한 지식
    * 데이터를 잘 이해하면 의사소통이 잘 되고, 잘못된 시스템을 구축할 위험을 줄일 수 있음

### 9. 데이터 모델의 표기법인 ERD의 이해

* 데이터 모델 표기법
    * 1976년 피터 첸이 Entity-Relationship model이라는 표기법 만듦
    * IE표기법이 대세, Barker도 사용. 둘다 비슷함
* ERD 모델링 방법
    * 작업순서
        * 엔터티를 그린다
        * 엔터티를 적절하게 배치한다
        * 엔터티간 관계를 설정한다
        * 관계명을 기술한다
        * 관계의 참여도를 기술한다
        * 관계의 필수여부를 기술한다
    * 배치방법
        * 사람이 왼쪽 위부터 보니까 가장 중요한 엔터티를 왼쪽상단 배치
        * 가장 중요한 엔터티를 왼쪽상단 조금 아래쪽 중앙에 배치하면 선이 안꼬임
    * ERD 관계의 연결
        * Primary Key로 속성이 상속되는 식별자 관계 설정
        * 중복되는 관계, Circle 관계 발생하면 안됨
    * ERD 관계명의 표시
        * 현재형 사용, 지나치게 포괄적인 용어(이다, 가진다)사용 자제
    * ERD 관계 관계차수와 선택성 표시
        * 1:1 관계는 실선 표시
        * Many 관계는 까마귀발 표현
        * 필수/선택은 관계선에 원으로 표현
  
### 10. 좋은 데이터 모델의 요소

* 완전성: 업무에서 필요한 모든 데이터가 데이터 모델에 정의
* 중복배제: 동일한 사실은 한 번만 기록
* 업무규칙: 업무규칙을 데이터 모델에 표현하고, 모든 사용자가 공유
* 데이터 재사용: 데이터 통합성, 독립성에 대해 충분히 고려하여 회사 전체의 관점에서 공동 데이터 도출
* 의사소통: 많은 관련자들이 설계자가 정의한 업무 규칙을 동일한 의미로 받아들이고 의사소통 도구로서 활용
* 통합성: 전체 조직관점에서 중복된 데이터를 배제할 수 있도록 공동 사용에 용이하게 정의

## 제 2절. 엔터티

### 1. 엔터티의 개념

* 업무에 필요하고 유용한 정보를 저장하고 관리하기 위한 집합적인 것
* 특성을 설명할 수 있는 속성을 가짐
* 인스턴스의 집합(ex. 과목 엔터티의 인스턴스는 수학, 영어, 과학)
* 눈에 보이지 않는 것이 엔터티로 도출되므로 주의

### 2. 엔터티와 인스턴스에 대한 내용과 표기법

* 사각형으로 표현
* 엔터티는 인스턴스의 집합

### 3. 엔터티의 특징

* 엔터티가 엔터티의 성질을 만족하지 못하면 적절하지 않은 엔터티
    * 업무에서 필요로 하는 정보
        * 업무영역에서 쓰이는 정보여야 함
    * 식별 가능해야 함
        * 인스턴스만의 고유한 이름인 식별자에 의해 식별이 가능해야 함 
    * 인스턴스의 집합
    * 업무프로세스에 의해 이용되어야 함
    * 속성을 포함
    * 관계의 존재
        * 관계를 생략하는 경우: 통계를 위한 엔터티, 코드를 위한 엔터티, 내부 필요에 의한 엔터티(트랜잭션 로그 테이블)

### 4. 엔터티의 분류

* 유무형에 따른 분류
    * 유형 엔터티
        * 물리적인 형태가 있고 안정적이며 지속적으로 활용되는 엔터티
        * 사원, 물품, 강사 등이 해당
    * 개념 엔터티
        * 물리적인 형태가 없고, 관리해야 될 개념적 정보로 구분
        * 조직, 보험상품 등이 해당
    * 사건 엔터티
        * 업무를 수행함에 따라 발생하는 엔터티. 발생량이 많고 통계자료에 이용
        * 주문, 청구, 미남 등이 해당
* 발생시점에 따른 분류
    * 기본 엔터티
        * 업무에 원래 존재하는 정보
        * 다른 엔터티와 관계에 의해 생성되지 않음
        * 고유한 주식별자
        * 타 엔터티의 부모 역할
        * 사원, 부서, 고객, 상품, 자재 등
    * 중심 엔터티
        * 기본엔터티로부터 발생되고 업무에 있어 중심적인 역할
        * 계약, 사고, 예금원장, 청구, 주문, 매출 등
    * 행위엔터티
        * 두 개 이상의 부모엔터티로부터 발생
        * 자주 내용이 바뀌고 데이터양이 증가
        * 초기단계에서는 나타나지 않으며 상세 설계, 상관 모델링 시 도출
        * 주문목록, 사원변경이력
* 스스로 생성될 수 있는지 여부에 따라: 독립엔터티, 의존엔터티

### 5. 엔터티의 명명

* 현업업무에서 사용하는 용어
* 약어 사용 지양
* 단수명사 활용
* 모든 엔터티에서 유일하게 이름 부여
* 엔터티 생성의미대로 이름 부여: 못지키는 경우 많음

## 제 3절. 속성(Attribute)

### 1. 속성의 개념

* 정의
    * 업무에서 필요로 함
    * 의미상 더 이상 분리되지 않음
    * 엔터티를 설명하고 인스턴스의 구성요소가 됨 

### 2. 엔터티, 인스턴스와 속성, 속성값에 대한 내용과 표기법

* 엔터티, 인스턴스, 속성, 속성값의 관계
    * 한 개의 엔터티는 두 개 이상의 인스턴스의 집합이어야 한다
    * 한 개의 인스턴스는 두 개 이상의 속성을 갖는다
    * 한 개의 속성은 한 개의 속성값을 갖는다
    * 예시
        * 사원 엔터티는 홍길동, 홍길자 인스턴스를 가짐
        * 홍길동 인스턴스는 이름, 주소, 전화번호, 직책 속성을 가짐
        * 홍길동, 서울시 강남구, 123-4567, 대리는 속성값
* 속성의 표기법: 엔터티 내 이름을 포함하여 표현

### 3. 속성의 특징

* 속성은 특징을 가지고 있으며, 아래 성질을 만족하지 못하면 적절하지 않음
    * 해당 업무에서 필요하고 관리하고자 하는 정보여야 함
    * 정규화 이론에 근간하여 정해진 주식별자에 함수적 종속성을 가져야 한다
    * 하나의 속성에는 한 개의 값만을 가짐. 다중값일 경우 별도의 엔터티를 이용하여 분리

### 4. 속성의 분류

* 특성에 따른 분류
    * 기본속성
        * 업무로부터 추출된 속성
        * ex. 제품이름, 제조년월, 제조원가
        * 업무로부터 추출되었지만 코드로 정의한 속성은 기본속성이 아님
    * 설계속성
        * 데이터 모델링, 업무 규칙화를 위해 새로 만들거나 변형하여 정의한 속성
        * ex. 약품용기코드, 일련번호
    * 파생속성
        * 다른 속성에 영향을 받아 발생, 계산된 값
        * ex. 전체용기 수, 용기의 총금액
        * 가급적 적게 정의
* 구성방식에 따른 분류
    * PK(Primary Key)속성: 엔터티를 식별할 수 있는 속성
    * FK(Foreign Key)속성: 다른 엔터티와의 관계에서 포함된 속성
    * 일반속성: 둘다 아닌 속성
* 기타 분류방법
    * 세부 의미를 쪼갤 수 있는지 여부에 따른 분류: 단순형 / 복합형(주소와 같이 시/구/동/번지로 나뉨)
    * 단일값(값이 한 개) / 다중값(집전화, 휴대전화, 회사 전화번호 / 1차 정규화 또는 별도 엔터티 생성)

### 5. 도메인

* 각 속성은 가질 수 있는 값의 범위가 있음
    * ex. 학점: 0.0~4.3 실수
    * 속성에 대한 데이터타입, 크기, 제약사항을 지정

### 6. 속성의 명명

* 원칙
    * 해당업무에서 사용하는 이름 부여
    * 서술식 속성명 사용금지
    * 약어사용 제한
    * 전체 데이터 모델 내 유일성 확보

## 제 4절. 관계(Relationship)

### 1. 관계의 개념

* 관계의 정의
    * 엔터티의 인스턴스 사이의 논리적인 연관성
    * 존재의 형태로서나 행위로서의 서로에게 연관성이 부여된 상태
* 관계의 페어링
    * 관계는 엔터티 안에 인스턴스가 개별적으로 관계를 가지는 것(페어링)
    * 이것의 집합을 관계로 표현
    * 관계(집합) - 어커런스(개별, 엔터티의 인스턴스와 같은 개념)

### 2. 관계의 분류

* 존재에 의한 관계
    * ex. 사원은 부서에 항상 속해있다
    * UML 클래스다이어그램: 연관관계, 실선
* 행위에 의한 관계
    * ex. 주문은 고객이 주문을 할 때 발생한다
    * URL 클래스다이어그램: 의존관계, 점선

### 3. 관계의 표기법

* 관계명: 관계의 이름
    * 두 개의 관계명을 가짐: 부서(포함한다) - (소속된다)사원
    * 시작되는 점을 관계시작점, 받는 편을 관계끝점이라고 하는데, 모두 관계이름 가져야 함
    * 명명규칙
        * 애매한 동사 피함
        * 현재형으로 표현
* 관계차수
    * 관계에서의 참여자의 수를 표현
    * 1:1 관계: 실선
    * 1:M 관계: M 쪽에 까마귀발
    * M:M 관계: 양쪽 까마귀발, 관계엔터티를 이용하여 3개의 엔터티로 구분
* 관계선택사양
    * 필수(Mandatory)관계 > 필수참여, 선택(Optional)관계 > 선택참여
    * ERD에서는 선택참여 하는 쪽을 원으로 표시
    * Foriegn Key로 연결될 경우 Null을 허용하는 항목

### 4. 관계의 정의 및 읽는 방법

* 관계 체크사항
    * 두 개의 엔터티 사이에 관심있는 연관규칙이 존재하는가?
    * 두 개의 엔터티 사이에 정보의 조합이 발생되는가?
    * 업무기술서, 장표에 관계연결을 위한 규칙이 서술되어 있는가?
    * 업무기술서, 장표에 관계연결을 가능하게 하는 동사가 있는가?
* 관계 읽기

    | 각각의/하나의 | 기준엔터티 | 관계차수 | 관련엔터티 | 선택사양<br>(필수/선택) | 관계명   |
    |:--------------|:-----------|:---------|:-----------|:------------------------|:---------|
    | 각각의        | 사원은     | 한       | 부서에     | 항상                    | 속한다   |
    | 각            | 부서에는   | 여러     | 사원이     | 때때로                  | 소속된다 |

## 제 5절. 식별자

### 1. 식별자(Identifiers) 개념

* 인스턴스들을 담고 있는 엔터티 내에서 인스턴스들을 구분할 수 있는 구분자
* 하나에 엔터티에 구성되어 있는 여러 개의 속성 중 엔터티를 대표할 수 있는 속성

### 2. 식별자의 특징

* 주식별자의 특징
    * 유일성: 엔터티 내의 모든 인스턴스들이 주식별자에 의해 유일하게 구분되어야 함
    * 최소성: 주식별자를 구성하는 속성의 수는 유일성을 만족하는 최소의 수
    * 불변성: 지정된 주식별자의 값은 자주 변하지 않는 것이어야 함
    * 존재성: 주식별자가 지정되면 값이 반드시 들어와야 함

### 3. 식별자 분류 및 표기법

* 식별자 분류
    * 대표성 여부
        * 주식별자: 엔터티 내에서 각 어커런스를 구분할 수 있는 구분자, 타 엔터티와 참조관계를 연결할 수 있는 식별자
        * 보조식별자: 각 어커런스를 구분할 수 있는 구분자이나, 대표성을 가지지 못해 참조관계 연결을 못함
    * 스스로 생성여부
        * 내부식별자: 엔터티 내부에서 스스로 만들어지는 식별자
        * 외부식별자: 타 엔터티와의 관계를 통해 타 엔터티로부터 받아오는 식별자
    * 속성의 수
        * 단일식별자: 하나의 속성으로 구성된 식별자
        * 복합식별자: 둘 이상의 속성으로 구성된 식별자
    * 대체여부
        * 본질식별자: 업무에 의해 만들어지는 식별자
        * 인조식별자: 업무적으로 만들어지지는 않지만 원조식별자가 복잡한 구성을 가지고 있기 때문에 인위적으로 만든 식별자

### 4. 주식별자 도출기준

* 해당 업무에서 자주 이용되는 속성을 주식별자로 지정
    * ex. 사원번호가 직원을 관리할 때 흔히 사용하므로 주식별자로 지정. 주민번호도 식별가능한 속성이지만 관리에 사용하지 않으므로 보조식별자로 사용
* 명칭, 내역 등과 같이 이름으로 기술되는 것은 피함
    * ex. 부서이름 대신 부서코드로 식별
* 속성의 수가 많아지지 않도록 함
    * 주식별자의 속성 수가 많으면 새로운 인조식별자를 생성하여 데이터 모델을 구성
    * ex. 주식별자로 (접수일자, 관할부서, 입력자사번, 접수방법코드 ...) 대신 (접수번호(부서+접수일자+일련번호)) 사용

### 5. 식별자관계와 비식별자관계에 따른 식별자

* 식별자관계와 비식별자 관계의 결정
    * 엔터티에 주식별자가 지정되고 엔터티간 관계를 연결하면 부모쪽의 주식별자를 자식엔터티의 속성으로 내려보냄
* 식별자관계
    * 부모로부터 받은 식별자를 자식엔터티의 주식별자로 이용
* 비식별자관계
    * 부모로부터 받은 식별자를 일반적인 속성으로만 사용함
    * 부모 없는 자식이 생성될 수 있는 경우
    * 자식만 남겨두고 부모가 먼저 소멸될 수 있는 경우
    * 여러 개의 엔터티가 하나의 엔터티로 통합되었는데, 각각의 엔터티가 별도의 관계를 가질 때
        * ex. 방문접수(접수번호, 주민번호), 인터넷접수(접수번호, 전자메일), 전화접수(접수번호, 전화번호) 엔터티를 접수 엔터티로 통합시 식별자로 접수번호를 가지고, 전화번호, 주민번호, 전자메일ID를 비식별자 관계로 표기
    * 자식엔터티에 주식별자로 사용해도 되지만 별도의 주식별자를 생성하는 것이 더 유리할 때
* 식별자 관계로만 설정할 때의 문제
    * 부모엔터티에서 자식엔터티로 내려갈수록 PK속성의 수가 증가함
    * where절의 길이가 길어짐
* 비식별자 관계로만 설정할 때의 문제
    * 자식엔터티에서 부모엔터티로의 조인 발생
* 식별자관계와 비식별자관계 모델링
    * 비식별자관계 선택 프로세스
        * 식별/비식별 취사선택은 내공이 필요
        * 기본적으로 식별자관계로 모든 관계를 연결하면서 다음 조건에 해당할 경우 비식별자관계로 주정
            * 관계가 약함
            * 자식테이블 독립 PK 필요
            * SQL 복잡도가 증가하여 개발생산성 저하
    * 식별자와 비식별자관계 비교
        
        | 항목               | 식별자관계                                                                                                                 | 비식별자관계                                                                                                                                                                              |
        |:-------------------|:---------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
        | 목적               | 강한 연결관계 표현                                                                                                         | 약한 연결관계 표현                                                                                                                                                                        |
        | 자식 주식별자 영향 | 자식 주식별자 구성에 포함                                                                                                  | 자식 일반 속성에 포함                                                                                                                                                                     |
        | 표기법             | 실선 표현                                                                                                                  | 점선 표현                                                                                                                                                                                 |
        | 연결 고려사항      | -반드시 부모엔터티 종속<br>-자식 주식별자 구성에 부모 주식별자 포함 필요<br>-상속받은 주식별자속성을 타 엔터티에 이전 필요 | -약한 종속관계<br>-자식 주식별자구성을 독립적으로 구성<br>-자식 주식별자구성에 부모 주식별자 부분 필요<br>-상속받은 주식별자속성을 타 엔터티에 차단 필요<br>-부모쪽의 관계참여가 선택관계 |
        