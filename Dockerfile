FROM centos:7

ADD http://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel7.repo /etc/yum.repos.d/
ADD http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor /tmp/
RUN rpm --import /tmp/RPM-GPG-KEY-HTCondor

RUN yum install -y \
    condor \
    condor-python \
    && yum -y clean all

ADD https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-init_1.0.1_amd64 /bin/dumb-init
RUN chmod +x /bin/dumb-init

RUN mkdir /run/lock
