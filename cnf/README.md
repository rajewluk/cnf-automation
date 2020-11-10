1. Przejdź do cnf-automation `cd cnf-automation`  
   Zainstaluj pakiety `pipenv install`  
   Uruchom wirtualne środowisko `pipenv shell`  
   Przejdz do katalogu cnf/ `cd cnf`
2. Dodaj kubeconfig dla klastra ONAP i klastra w którym ma byc instancjonowany vFW:
   - `artifacts/cluster_kubeconfig`
   - `artifacts/onap_kubeconfig`
3. Zmodyfikuj w `config.py`:
   - CLOUD_REGION
   - GLOBAL_CUSTOMER_ID
   - VENDOR
   - SERVICENAME
4. uruchom skrypt tworzący **CloudRegion** `python create_k8s_region.py`  
5. Zaonboarduj **vFW** `python onboarding.py`
6. Zainstancjonuj **vFW** `python instantiation.py`
