from dcos.mesos import Slave, Task

import mock


def task_fixture():
    """ Task fixture

    :rtype: Task
    """

    task = Task({
        "executor_id": "",
        "framework_id": "20150502-231327-16842879-5050-3889-0000",
        "id": "test-app.d44dd7f2-f9b7-11e4-bb43-56847afe9799",
        "labels": [],
        "name": "test-app",
        "resources": {
            "cpus": 0.1,
            "disk": 0,
            "mem": 16,
            "ports": "[31651-31651]"
        },
        "slave_id": "20150513-185808-177048842-5050-1220-S0",
        "state": "TASK_RUNNING",
        "statuses": [
            {
                "state": "TASK_RUNNING",
                "timestamp": 1431552866.52692
            }
        ]
    }, None)

    task.user = mock.Mock(return_value='root')
    slave = Slave({"hostname": "mock-hostname"}, None, None)
    task.slave = mock.Mock(return_value=slave)
    return task
