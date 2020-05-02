import nvidia.dali as dali
'''
Video I/O source based on NVIDIA's excellent DALI framework
Requirements: Linux only, GPU only!
'''


class DaliVideoPipe(dali.Pipeline):
    def __init__(self, batch_size, num_threads, device_id, data, shuffle, sequence_length, initial_prefetch_size):
        super(DaliVideoPipe, self).__init__(batch_size, num_threads, device_id, seed=16)
        self.input = dali.ops.VideoReader(device="gpu", filenames=data, sequence_length=sequence_length,
                                          shard_id=0, num_shards=1,
                                          random_shuffle=shuffle, initial_fill=initial_prefetch_size)

        # self.transpose = ops.Transpose(device="gpu", perm=[0, 3, 1, 2])

    def define_graph(self):
        raw_img = self.input(name="Reader")
        # trans_img = self.transpose(raw_img)
        return raw_img

