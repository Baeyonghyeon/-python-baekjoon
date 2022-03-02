# 1 준비
# 이름 : 배용현
# 과정 : 자바 웹 백엔드
# 날짜 : 3월 1일 ~

# 2 계산 절차를 간추리는 방법
def fold(identity, glue, xs):
    result = identity
    for x in xs:
        result = glue(result, x)
    return result


# sum_integers를 활용해 배열을 만들어 xs로 넘겨준다.
# sum
sum = lambda xs: fold(0, lambda x, y: x + y, xs)
sum_integers = lambda a, b: sum([i for i in range(a, b + 1)])
print(sum_integers(1, 10))
# product
product = lambda xs: fold(1, lambda x, y: x * y, xs)
product_integers = lambda a, b: product([i for i in range(a, b + 1)])
print(product_integers(1, 10))

from random import random

n = 20
print(sum(random() for _ in range(0, n)))
print(product(random() for _ in range(0, n)))


# 3 스트림 (모르겠다 8ㅅ8)
def delay(v):
    return lambda: v


def force(v):
    return lambda: v


EmptyStream = None


def stream(x, xs):  # const_stream
    return (x, delay(xs))


def head(stream):
    (x, _) = stream
    return x


def tail(stream):
    (_, xs) = stream
    return force(xs)


def integers(a, b):
    if a > b: return EmptyStream
    return stream(a, [i for i in range(a, b + 1)])


def foreach(f, stream):
    if stream == EmptyStream:
        return None
    else:
        foreach(f, head(stream))
    return foreach(f, tail(stream))

#3.2 대안을 찾아서
def integers_from(n):
    while True:
        yield(n)
        n+1