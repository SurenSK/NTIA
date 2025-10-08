import torch
import glob

files=sorted(glob.glob("res_gpu_*.pt"))
if not files:
    print("No intermediate tensor files found matching 'res_gpu_*.pt'")
else:
    tensors=[torch.load(f,map_location='cpu') for f in files]
    res=torch.cat(tensors,dim=0)
    
    res=res.max(dim='window').values
    no_relation_scores=res[0]
    real_relation_scores=res[1:]
    max_real_relation_scores,_=torch.max(real_relation_scores,dim='relationship')
    strong_relation_mask=max_real_relation_scores>-2.5
    res[0,strong_relation_mask]=-torch.inf
    final_relationships=res.argmax(dim='relationship')
    
    torch.save(final_relationships,'final_relationships.pt')
    print(f"Loaded {len(files)} tensors. Saved result to final_relationships.pt")