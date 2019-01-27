FROM amazonlinux:2.0.20190115
# set timezone
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN yum install -y tar gzip

RUN curl -O https://dl.google.com/go/go1.11.5.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf go1.11.5.linux-amd64.tar.gz
# RUN rm -f go1.11.5.linux-amd64.tar.gz
# RUN export PATH=$PATH:/usr/local/go/bin

# set LANG
# ENV LANG ja_JP.UTF-8

ENTRYPOINT ["/usr/local/go/bin/go", "version"]