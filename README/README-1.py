"""
MVC 패턴

Model : DTO(data transfer object) + DAO(data access object)
Service : Business Logic(Algorithm)
Controller : RESTful 방식으로 React Axios로 통신

모델-뷰-컨트롤러 패턴 (Model-View-Controller pattern)
MVC 패턴이라고도 하는 이 패턴은 대화형 어플리케이션(INTERACTIVE APPLICATION)을 다음의 3 부분으로 나눈다.

모델(Model) - 핵심 기능과 데이터를 포함한다.
    - Service, Model
        - DTO, DAO -> orm
        - Model(*.py - memory) : Machine(*.h5 disk) 저장된 형태
        - Service : 저장된 모델을 호출하여 기능을 수행하게 하는 파트
뷰(View) - 사용자에게 정보를 표시한다(하나 이상의 뷰가 정의도리 수 있음)
컨트롤러(Controller) - UI로부터 입출력을 처리한다.


AI-Calc 에서 사칙연산을 나누는 이유
머신 model-* 은 history를 기억하는 능력이 있다.
5 + 2 = 7
5 + * = *

...

5 덧셈연산을 제안...

그 후 7 곱셉연산을 제안했을 때
연산 단위로 체크포인트에 히스토리를 갖고 있다.


텐서에서 변수의 저장은 확률변수




"""