# consul-connect-sidecar-example
Hashicorp Consul Connect Sidecar Example

## Requires

1. Hashicorp Consul 1.4.0
2. Docker
3. docker-compose
4. Python flask
5. Golang

## Install

[Install Consul](https://www.consul.io/docs/install/index.html)
[Install Docker](https://docs.docker.com/install/linux/docker-ce/binaries/)
[Install docker-compose](https://docs.docker.com/compose/install/)
[Install Golang](https://golang.org/doc/install)

Install Python Framework flask according to the platform of each LInux OS.

## Usage

### Consul

Start / Stop Consul Process 

```bash
$ systemctl start consul
$ systemctl stop consul
```

### Consul Sidecar

Start Side Car

1. hoge
```bash
$ consul connect proxy -sidecar-for hoge
```

2. page
```bash
$ consul connect proxy -sidecar-for page
```

### Consul Sidecar Proxy

3. nginx
```bash
$ consul connect proxy -sidecar-for nginx
```

### Confirm

```bash
$ curl http://localhost:<SERVICE?PORT>/hoge
$ curl http://localhost:<SERVICE?PORT>/page
```

