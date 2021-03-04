# HTML / CSS / JavaScript Note

## CSS

### 1. Selector (선택자)

- 기본 구조

> <pre>
> <code>
> selector {
>   property: value
> }
> //property와 value 쌍은 여러개가 올 수 있다.
> </code>
> </pre>

- 종류

1. id

> > id에 관한 css는 selector 앞에 #을 추가한다

> >  <pre>
> >  <code>
> >  #selector {
> >    property: value
> >  }
> >  </code>
> >  </pre>

2. 부모 자식 Selector

> >  <pre>
> >  <code>
> >  parent child {
> >    property: value
> >  }
> >  </code>
> >  </pre>

> > - 부모 태그와 자식 태그를 바꿈

> >  <pre>
> >  <code>
> >  parent>child {
> >    property: value
> >  }
> >  </code>
> >  </pre>

> > - '>'가 붙으면 직계 자손만 바꿈

3. 가상 클래스 선택자

> - selctor:link - 방문한 적이 없는 링크
> - selctor:visited - 방문한 적이 있는 링크
> - selctor:hover - 마우스를 롤 오버 했을 때
> - selctor:acttive - 마우스를 클릭했을 때

> 이벤트가 동시에 발생하였을 때, css는 순서상 뒤의 코드를 무시한다. 따라서 순서에 신경을 써야한다.

### 2. 적용 순서

1. 상속

> Property 별로 상속이 되는것과 되지 않는 것이 있다.

2. Cascading

> 하나의 tag에 여러 css 효곽가 중첩되었을 때 우선순위는?

> 1. Style attribute
> 2. id selector
> 3. class selector
> 4. tag slector 순으로 우선순위를 가진다.

> 우선순위를 무시하고 싶다면 >> !important를 추가해준다.

### 3. 서채 다루기

1. Font Size

> - px
> - em
> - rem

rem이 가장 추천하는 단위, 다른 단위를 사용해야하는 명확한 이유가 없다면 rem을 사용하는 것이 좋다.

이유? 사용자가 브라우저 내에서 Font Size를 변경했을 때 rem을 제외한 나머지는 바뀌지 않는다.

2. Color

> - color name (red, blue...)
> - hex (#00FF00...)
> - rgb (rgb(0,0,0)...)

3. Text align

4. Font

5. web font (Google Fonts)

### 4. Layout

1. inline VS block level

> inline은 줄바꿈이 일어나지 않지만, block level은 줄바꿈이 일어난다.

2. box model

> inline 모델에서는 padding, margin은 적용 되지만 width, height 값은 적용되지 않는다.

3. box sizing

> width나 height를 같은 값으로 box를 생성해도 border값이 다르면 크기가 다르다.

> HTML은 내부의 값을 기준으로 생성하기 때문이다

> 따라서 border값과 관계 없이 생성하기 위해선 box-sizing을 이용하면 된다.

4. margin-collapsing

