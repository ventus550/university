uint32_t puzzle3(uint32_t n, uint32_t d){
	uint64_t num = n;
	uint64_t den = (uint64_t)d << 32;
	uint32_t edx = 32;
	uint32_t mask = 0x80000000;
	uint32_t result = 0;
	
	
	while(edx) {
        num*=2;
		if(num - den >= 0){
			result |= mask;
			num = num - den;
		}
		mask = mask >> 1;
		edx--;
	}
    return result;
}