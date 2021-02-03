FROM linuxserver/openssh-server

RUN apk update
RUN apk add gawk

COPY fs /mnt/bes/pcm
RUN mkdir /mnt/bes/pcm/tmp
RUN chmod -R 777 /mnt/
