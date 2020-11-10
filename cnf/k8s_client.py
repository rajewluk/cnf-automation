import os
from pprint import pprint

import oyaml as yaml
from kubernetes import config, client
from kubernetes.client import OpenApiException


class K8sClient:
    def __init__(self, kubeconfig_path):
        self.mypath = os.path.dirname(os.path.realpath(__file__))
        config.load_kube_config(config_file=os.path.join(self.mypath, kubeconfig_path))
        self.api_instance = client.CustomObjectsApi()

    def read_custom_object_file(self, file_path):
        with open(file_path) as crd_file:
            crd_body = yaml.load(crd_file, Loader=yaml.FullLoader)
        return crd_body

    def get_custom_object_details(self, crd_body):
        group = crd_body["apiVersion"].split("/")[0]
        version = crd_body["apiVersion"].split("/")[1]
        plural = crd_body["kind"].lower() + "s"
        name = crd_body["metadata"]["name"]

        return group, version, plural, name

    def create_custom_object(self, file_path):
        crd_body = self.read_custom_object_file(file_path)
        group, version, plural, name = self.get_custom_object_details(crd_body)
        api_response = None
        try:
            api_response = self.api_instance.create_cluster_custom_object(group=group,
                                                                          version=version,
                                                                          plural=plural,
                                                                          body=crd_body,
                                                                          pretty="true")
        except OpenApiException as error:
            print(str(error.status) + " " + error.reason)
            pprint(error.body)
        return api_response
