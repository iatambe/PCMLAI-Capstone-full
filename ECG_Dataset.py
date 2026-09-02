
## Note: to handle issues with multiprocessing during training, I've put the ECG_Dataset class into its own separate python file.

import numpy as np
import torch

def load_sig_at_idx(i):
    return np.load(f'Data/Preprocessed/sig_{i}.npy')

class ECG_Dataset( torch.utils.data.Dataset ):
    
    def __init__(self, 
        labels ,
        all_sigs ,
        unknown_confidence_replace = 0.10 , # for imputing "unknown" confidence values. This is done BEFORE the threshold-based replacement.
        threshold = 0.00 , 
        # If threshold is None, don't do any threshold-based replacement at *this* stage.
        # If threshold  > 0 , any annotation with confidence >= threshold is treated as positive, otherwise negative.
        # If threshold == 0 , any annotation with confidence  > 0         is treated as positive, otherwise negative.
    ):
        assert callable(func_to_load_sig_at_idx)
        self.func_to_load_sig_at_idx = func_to_load_sig_at_idx
        
        assert len(labels.shape)==1
        self.labels = labels

        assert 0.0<=unknown_confidence_replace<=1.0
        self.unknown_confidence_replace = unknown_confidence_replace
        
        if threshold is not None :
            assert 0.0<=threshold<=1.0
        self.threshold = threshold

        assert all_sigs.ndim==3 and all_sigs.shape[1]==12 and all_sigs.shape[1]==5000 , \
            "The all_sigs parameter for the ECG_Dataset class constructor must be of shape (N,12,5000)"
        self.all_sigs = all_sigs

    def __len__(self):
        return self.labels.shape[0]

    def __getitem__(self, idx):
        # Note: output must be pair of torch tensors.

        x_np = self.all_sigs[idx]
        x = torch.tensor(x_np, dtype=torch.float32)

        y = np.array( self.labels[idx] , dtype=np.float32 )
        y[ y == -1.0 ] = self.unknown_confidence_replace
        if self.threshold is not None :
            if self.threshold == 0.0 :
                y = (y > 0.0).astype(np.float32)
            else :
                y = (y >= self.threshold).astype(np.float32)
        y = torch.tensor(y)
        
        return x , y




        