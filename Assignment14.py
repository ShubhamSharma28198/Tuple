#ques1-->
f=open('xyz.txt','r',encoding='utf8')
d=f.readlines()
print("last line is-->",d[-1])

#ques2-->
f=open('xyz.txt','r',encoding='utf8')
d=f.readlines()
words=[]
for line in d:
    words=words+(line.split())
print(words)
for w in words:
    print(w)
f.close()

#ques3-->
with open("xyz.txt",encoding='utf8') as f:
    with open("out.txt", "w",encoding='utf8') as f1:
        for line in f:
            f1.write(line)
#ques4-->
with open('xyz.txt',encoding='utf8') as fh1, open('out.txt',encoding='utf8') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)

#ques5-->
import random
f=open('Random.txt','w')
for i in range(10):
    data=str(random.randint(1,10))
    f.write(data)
    f.write("\n")
f.close()
print("\nReading the file now")
file1 = open("Random.txt",'r')
file2 = open("sorted.txt",'w')
list1=file1.readlines()
list1.sort()
file2.writelines(list1)
file1.close()
file2.close()

'''
#OUTPUT-->
#1-->
last line is--> That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird
#2-->
['“Atticus', 'said', 'to', 'Jem', 'one', 'day,', '“I’d', 'rather', 'you', 'shot', 'at', 'tin', 'cans', 'in', 'the', 'backyard,', 'but', 'I', 'know', 'you’ll', 'go', 'after', 'birds.', 'Shoot', 'all', 'the', 'blue', 'jays', 'you', 'want,', 'if', 'you', 'can', 'hit', '‘em,', 'but', 'remember', 'it’s', 'a', 'sin', 'to', 'kill', 'a', 'mockingbird.”', 'That', 'was', 'the', 'only', 'time', 'I', 'ever', 'heard', 'Atticus', 'say', 'it', 'was', 'a', 'sin', 'to', 'do', 'something,', 'and', 'I', 'asked', 'Miss', 'Maudie', 'about', 'it.', '“Your', 'father’s', 'right,”', 'she', 'said.', '“Mockingbirds', 'don’t', 'do', 'one', 'thing', 'except', 'make', 'music', 'for', 'us', 'to', 'enjoy.', 'They', 'don’t', 'eat', 'up', 'people’s', 'gardens,', 'don’t', 'nest', 'in', 'corn', 'cribs,', 'they', 'don’t', 'do', 'one', 'thing', 'but', 'sing', 'their', 'hearts', 'out', 'for', 'us.', 'That’s', 'why', 'it’s', 'a', 'sin', 'to', 'kill', 'a', 'mockingbird.”', '–', 'Harper', 'Lee,', 'To', 'Kill', 'a', 'Mockingbird']
“Atticus
said
to
Jem
one
day,
“I’d
rather
you
shot
at
tin
cans
in
the
backyard,
but
I
know
you’ll
go
after
birds.
Shoot
all
the
blue
jays
you
want,
if
you
can
hit
‘em,
but
remember
it’s
a
sin
to
kill
a
mockingbird.”
That
was
the
only
time
I
ever
heard
Atticus
say
it
was
a
sin
to
do
something,
and
I
asked
Miss
Maudie
about
it.
“Your
father’s
right,”
she
said.
“Mockingbirds
don’t
do
one
thing
except
make
music
for
us
to
enjoy.
They
don’t
eat
up
people’s
gardens,
don’t
nest
in
corn
cribs,
they
don’t
do
one
thing
but
sing
their
hearts
out
for
us.
That’s
why
it’s
a
sin
to
kill
a
mockingbird.”
–
Harper
Lee,
To
Kill
a
Mockingbird

#3-->
out.txt-->
“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.”
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird



#4-->
“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.
“Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds.

Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.”
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.”

That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it.

“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.
“Your father’s right,” she said. “Mockingbirds don’t do one thing except make music for us to enjoy.

They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us.

That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird
That’s why it’s a sin to kill a mockingbird.” – Harper Lee, To Kill a Mockingbird

#5-->
Reading the file now


Random.txt-->
6
5
8
4
9
5
10
6
1
3

Sorted.txt-->
1
10
3
4
5
5
6
6
8
9
