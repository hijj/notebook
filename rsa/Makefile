

CC = gcc
CFLAGS = -Wall -g -O0 -I/usr/local/openssl111f/include
LIBS = -L/usr/local/openssl111f/lib -lcrypto
OBJ = rsa_test.o
RM = rm -f

rsa_test:$(OBJ)
	$(CC) $(CFLAGS) $^ -o $@ $(LIBS)

%.o:%.c
	$(CC) $(CFLAGS) -c $< -o $@ 

clean:
	$(RM) *.o rsa_test
