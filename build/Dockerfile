FROM python:3.8.3
ARG version=latest
ARG branch=develop

RUN apt-get update
RUN ln -s /mnt/bes/pcm $HOME/ScenarioData

RUN pip install -U pip pipenv ipython jupyterlab ipywidgets

RUN git clone --single-branch --depth 1 --branch $branch \
    https://github.com/Breakthrough-Energy/PowerSimData
RUN git clone --single-branch --depth 1 --branch $branch \
    https://github.com/Breakthrough-Energy/PostREISE

WORKDIR /PowerSimData
RUN mkdir -p /mnt/bes/pcm
RUN mkdir -p /mnt/bes/pcm/data/input
RUN cp powersimdata/utility/templates/*.csv /mnt/bes/pcm/

COPY install.sh .
RUN ./install.sh $version

WORKDIR /app
RUN rm -rf /PowerSimData
RUN rm -rf /PostREISE

CMD ["jupyter", "lab", "--port=10000", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
