condor-docker
-------------

This creates a pretty basic condor docker image, including the python bindings. It's intended for running scripts against condor clusters using the python API.

For posterity, a script `htcondor-info.py` is included in the repository, which takes configuration through environment variables `COLLECTOR_URL` (which should be a host:port combo) and `SCHEDD_NAME` (which should be a hostname, usually). Assuming you've built this image with `-t htcondor` you could run, for example:

    docker run -e COLLECTOR_URL=condor-collector.example.com:9618 -e SCHEDD_NAME=condor-submit-node.example.com --rm -it -v $(pwd):/scripts -w /scripts htcondor python htcondor-info.py

You can run a `condor_master` in the container using `dumb-init`:

    docker run htcondor dumb-init /sbin/condor-master -f

You can, of course, also customize the config, potentially.
