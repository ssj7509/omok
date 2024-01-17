# Board Analyzer UML
![5 drawio](https://github.com/ssj7509/omok/assets/87068596/12b71402-6327-4765-8880-dad1ddb6f1df)
# 구현 기능
- 열림 닫힘 판별 : 오목에서 현재 돌의 형태를 연속으로 이어진 4개의 형태까지 발전시켰을 때, 양 옆이 모두 비어있는 경우가 있으면 열린 공격이다.
<br><br>
  - 열린 공격 2 : 노란색 원으로 표시한 부분이 두었을 때 열린 공격 2가 되는 자리들이다.
![image](https://github.com/ssj7509/omok/assets/87068596/b37c4ce0-bead-4ff2-9830-442a1f08e491)
<br><br>

  - 닫힌 공격 2 : 두었을 때 닫힌 공격 2가 되는 자리들이다.
![image](https://github.com/ssj7509/omok/assets/87068596/6e5ee77b-68ea-4d1b-b9b9-7e3d73a1f942)
<br><br><br>


- 렌주 룰 금수 자리 판별 : 렌주 룰에서는 흑에게만 33, 44, 육목이 금지된다.
<br><br>
  - 33 금수 : 흑의 열린 2가 두 개 이상 겹치는 자리는 33 금수 자리이다.
![image](https://github.com/ssj7509/omok/assets/87068596/a04e6070-4293-4981-b9da-01bdbb076ae6)
<br><br>
  - 44 금수 : 흑의 3 자리가 두 개 이상 겹치는 자리는 44 금수 자리이다. 열린 경우와 닫힌 경우 상관없이 모두 금수로 처리된다.
![image](https://github.com/ssj7509/omok/assets/87068596/ac937013-25cb-4f1a-a72f-dac493af24c7)
<br><br>
  - 육목 금수 : 흑이 두었을 때 연속으로 6개가 이어지는 형태의 자리는 육목 금수 자리이다.
![image](https://github.com/ssj7509/omok/assets/87068596/b4d530bc-5363-4449-8197-ba40038c72c8)

<br><br><br>
- Trigger - Target 알고리즘 : 43 공격과 같은 겹침 공격을 빌드업하기 위한 과정이다. Trigger 자리에 유효한 수가 겹친다면, 그 겹친 수의 수치를 Target 자리로 복사한다. 수가 겹친 자리와 Target 자리에 동일한 우선순위를 부여하여, 이후 더 큰 수가 겹칠 수 있는 가능성이 열린다.
<br><br>
  - 파란색 화살표가 가리키는 자리가 열린 1의 Target 자리이며, 현재 열린 1(Trigger) 자리에 닫힌 3 공격이 겹쳐있으므로 Target 자리로 닫힌 공격 3의 수치를 복사한다. 아래의 경우에는 겹친 자리와 Target으로 수치가 복사된 자리가 같은 수치를 가진다.
![image](https://github.com/ssj7509/omok/assets/87068596/4515c938-9a8b-4096-aa3f-c00b23ca3e7d)
<br><br>
  - 만약 위 형태에서 Target 자리에 또다른 유효한 수가 겹쳐있다면, 우선순위는 Target 자리가 높아지게 되어 Target 자리에 두게 된다. 아래의 빨간 점 위치가 유효 수(공격 2)가 겹친 Target 자리이다.
    ![image](https://github.com/ssj7509/omok/assets/87068596/aec97b12-7a1d-4398-9166-618599c94bba)
<br><br>
  - 위 상황에서 상대는 Target 자리와 겹쳐있던 유효한 수(공격 3) 자리를 강제로 막게 된다.
  ![image](https://github.com/ssj7509/omok/assets/87068596/ad503c4f-e131-4552-ae6a-03faefa8e9e7)
<br><br>
  - 상대가 강제로 Target에 겹쳐있는 또다른 수를 막게 되면, 흑이 43 공격을 할 수 있게 된다.(아래의 빨간 점 위치)
![image](https://github.com/ssj7509/omok/assets/87068596/a83d5492-a696-4b7e-986d-742b7d050e7c)

