Name: Aaditya Pramod

Email: aaditya2002pramod@gmail.com

Description:

While testing for the coverpoints for a given ISA string, we need to check if the relevant bits of misa register have been set or not. We first get the ISA string from the user as an input and then
process it to get various relevant parts of the ISA string like the xlen and the extensions used. Then we check the extensions being used and generate coverpoints for each of them. We can also combine the
conditions for a set of coverpoints to reduce the number of check we need to perform. These generated conditions are wwritten as part of the csr_comb covergroup in the yaml file.
