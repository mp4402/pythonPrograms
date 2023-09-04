import numpy as np
import cython
@cython.boundscheck(False)
cpdef unsigned char[:, :] apply_kernel_cythonized(unsigned char[:, :] img, unsigned char[:, :] kernel):
    cdef int k_r, k_c, x, y, R, r, c, i , j, t
    cdef unsigned char[:, :] n
    
    k_r = kernel.shape[0]
    k_c = kernel.shape[1]

    R = k_r//2
    
    r = img.shape[0]
    c = img.shape[1]

    for i in range(R, r-R):
        for j in range(R, c-R):
            n = img[i-R:i+R+1, j-R:j+R+1]
            
            # numpy
            #t = np.multiply(n, kernel).sum()

            # loop
            t = 0
            for x in range(k_r):
                for y in range(k_c):
                        t += n[x, y] * kernel[x, y]
                        
            img[i,j] = t
    
    return img
