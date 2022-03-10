ARG build_env=release
FROM python:3.8.3 as base
ARG version=latest

RUN apt-get update
RUN ln -s /mnt/bes/pcm $HOME/ScenarioData

RUN pip install -U pip pipenv ipython jupyterlab ipywidgets


FROM base as build_release
ONBUILD RUN git clone --depth 1 https://github.com/Breakthrough-Energy/PowerSimData; \
    git clone --depth 1 https://github.com/Breakthrough-Energy/PostREISE

FROM base as build_debug
ONBUILD COPY PowerSimData .
# ONBUILD COPY PostREISE .

FROM build_$build_env

WORKDIR /PowerSimData
# RUN mkdir -p /mnt/bes/pcm
RUN cp powersimdata/utility/templates/*.csv /mnt/bes/pcm/

# COPY install.sh .
# RUN ./install.sh $version

WORKDIR /app
RUN rm -rf /PowerSimData
# RUN rm -rf /PostREISE

CMD ["jupyter", "lab", "--port=10000", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
