python3 inference.py  \
        --base_model ./data/models/LongAlpaca-7B \
        --question "Generate a meta review based on the peer reviews." \
        --context_size 32768 \
        --max_gen_len 512 \
        --material ./materials/peer.txt