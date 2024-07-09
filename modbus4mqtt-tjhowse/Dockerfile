FROM ghcr.io/jesseklm/modbus4mqtt:master

COPY run.py /
RUN chmod a+x /run.py

ENTRYPOINT [ "/run.py" ]
