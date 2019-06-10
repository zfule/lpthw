#正话反说
def pinjie(*sts):
    st1, st2, st3 = sts
    print(f"正话：{st1} {st2} {st3}")
    print(f"反说：{st3} {st2} {st1} \n")
    return st1 + st2 + st3

pinjie("我", "喜欢", "苹果")
dog = pinjie("A", "little", "dog")
snow = pinjie("snow", "is", "white")
ball = pinjie("What", "is", "ball")

print(f"Can you say that {dog} {snow}")

#This is ok?
thing = pinjie(dog, snow, ball)
print(thing)
