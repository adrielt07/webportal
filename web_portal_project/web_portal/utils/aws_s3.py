import boto3
import os


class S3ClientWebPortal:
    def __init__(self, company_id, company_name):
        """ Instantiate class 
        
        This is use for webportal interaction with AWS s3 resource

        credentials are read from ~/.aws/credentials

        https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html
        """
        self._s3_client = boto3.client('s3')
        self._bucket_name = os.environ.get('web_portal_prod_company_storage', 'web-portal-company-storage-dev')
        company_name = company_name.replace(' ', '_')
        self._root_object = f'{company_id}/{company_name}'
        self._s3_resource = boto3.resource('s3')
        


    def list_buckets(self):
        """ List all buckets """
        print('Existing buckets:')
        response = self._s3_client.list_buckets()
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')


    def get_all_objects(self, folder_name):
        """ retrieve company's s3 storage """
        mybucket = self._s3_resource.Bucket(self._bucket_name)
        prefix = f'/{self._root_object}/{folder_name}'
        objs = mybucket.objects
        return objs


    def create_folder_in_bucket(self, folder_name):
        """ Create a new folder inside the self._root_object
        
        Arg:
            folder_name <str>: name of the folder (ex: decom,)
        """
        s3_object_name = f'{self._root_object}/{folder_name}/'
        s3_obj = self._s3_client.put_object(Bucket=self._bucket_name, Key=s3_object_name)
        

if __name__ == "__main__":
    s3 = S3ClientWebPortal('1', 'ctrl-layer')
    s3.list_buckets()
    s3.create_folder_in_bucket('decom')
    obj = s3.get_all_objects('decom')
    print(dir(obj))
    data = obj.all()
    for i in data:
        print(i)
