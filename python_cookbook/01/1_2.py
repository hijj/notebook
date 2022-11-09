#!/usr/bin/python3
record=('Dave', 'dave@gmail.com', '777-4444', '888-4556')
name, email, *phone=record
print(phone)

records=[
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print("uname:", uname)
print("fields:", fields)


uname, *_, homedir, sh = line.split(':')
print("homedir:", homedir)

items = [1, 10, 7, 4, 5, 9]

def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head

print("sum:", sum(items))
