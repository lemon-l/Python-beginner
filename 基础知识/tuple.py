def damage(skill1,skill2):
    damage1 = skill1*3
    damage2 = skill2*2 + 10
    return damage1,damage2

#如果只是一个变量的话会返回元组，且之后看代码的时候不知道意义，最好用两个变量来接收它们
skill1_damage,skill2_damage = damage(3,6)
print(skill1_damage,skill2_damage)