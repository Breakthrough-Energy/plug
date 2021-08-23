FROM python:3.8.3

RUN apt-get update
RUN ln -s /mnt/bes/pcm $HOME/ScenarioData

RUN pip install -U pip pipenv ipython jupyterlab ipywidgets

RUN git clone --depth 1 https://github.com/Breakthrough-Energy/PowerSimData
RUN git clone --depth 1 https://github.com/Breakthrough-Energy/PostREISE

WORKDIR /PowerSimData
RUN mkdir -p /mnt/bes/pcm
RUN cp -r powersimdata/utility/templates /mnt/bes/pcm/

WORKDIR /PostREISE
RUN pipenv sync --dev --system;
RUN pip install .
RUN pip install ../PowerSimData

WORKDIR /app
RUN rm -rf /PowerSimData
RUN rm -rf /PostREISE

CMD ["jupyter", "lab", "--port=10000", "--no-browser", "--ip=0.0.0.0", "--allow-root"]