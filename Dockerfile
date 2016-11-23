FROM fedora:24
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>
RUN dnf clean all && \
    dnf -y install ImageMagick python-pip && \
    dnf clean all && \
RUN pip install PyPDF2 requests
