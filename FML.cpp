int random_bytes(unsigned char *out, size_t outlen){

    static HCRYPTPROV handle = 0;
    if(!handle){

	if(!CryptAcquireContext(&handle,0,0,PROV_RSA_FULL,
				CRYPT_VERIFYCONTEXT | CRYPT_SILENT)){

	    return -1;

	}

    }
    while(outlen > 0){

	const DWORD len = outlen > 1048576UL ? 1048576UL : outlen;
	if(!CryptGenRandom(handle, len, out)){

	    return -2;

	}
	out += len;
	outlen -= len;

    }
    return 0;
}