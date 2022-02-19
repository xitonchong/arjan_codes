from stream.data import BufferData 

# def dslr_camera() -> BufferData:
#     return "###DSLRDATA###"


class dslr_camera:
    def __call__(self, *args) -> BufferData: 
        return "### DSLR DATA ###"

    # repr built-in fuciton take precedent over __call__ method in Callable
    def __repr__(self, *args) -> BufferData: 
        print(" DSLR repr function")
        return self.__call__(*args)