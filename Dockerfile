FROM fedora:24
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>
RUN dnf clean all && \
    dnf -y install ImageMagick && \
    dnf clean all && \
RUN pip install PyPDF2==1.25.1 requests==2.9.1
