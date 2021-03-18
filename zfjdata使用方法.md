1、解压ZFJ——DATASET压缩包

2、运行zfj-dataprocess.py

3、下载glove

```
mkdir "glove_dir"
wget http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip -d "glove_dir"
```

4、export CUDA_VISIBLE_DEVICES=0,1

5、onmt_build_vocab -config zfj-config.yaml

6、onmt_train -config zfj-config.yaml