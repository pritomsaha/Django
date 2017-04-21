from django.conf import settings

def get_encoded_id(id):
	return settings.HASHID.encode(id)

def get_decoded_id(encoded_id):
	return settings.HASHID.decode(encoded_id)[0]