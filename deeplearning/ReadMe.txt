MainDeep.py
	特徴量学習を行うメインメソッド。
	実行すればすぐ使える。
	※学習させるファイルの形式
	label	x1	x2	x3	x4	…
	間はタブ。１行に１データ。
	==== method ====
	autoencoder(iteration, learning, x_length, y_length, filepath, prob)
		iteration : 試行回数
		learning : 学習率
		x_length : 入力のベクトル次元数
		y_length : 圧縮後のベクトル次元数
		prob : 欠損率(わざとデータの一部を破損させる)
		filepath : 学習ファイルパス
	encfile(filepath)
		filepath : 特徴量変換するファイルのデータ
	encoder(w_path, bias_path)
		w_path : autoencoderした結果の変換行列のファイル
		bias_path : autoencoderした結果の変換行列のバイアス値のファイル
	encfile(filepath)
		filepath : 特徴量変換するファイルのデータ

autoencoder.py
	特徴量学習。
	
encoder.py
	学習したファイルを使ってencode。
	
timecounter.py
	実行時間の出力
