from cancergeonomics.resources.base import Resource


class FileResource(Resource):

    def list(self, query_params=None):
        return self.api_client.get('files', query_params=query_params)

    def stat(self, file_id):
        return self.api_client.get(f'files/{file_id}')

    def update(self, file_id, data):
        return self.api_client.patch(f'files/{file_id}', data=data)

    def download(self, file_id, file_path):
        url = self.get_download_url(file_id)
        return self.api_client.download(url, file_path)

    def get_download_url(self, file_id):
        data = self.api_client.get(f'files/{file_id}/download_info')
        return data['url']
