# x_api

https://programming-zero.net/how-to-start-twitter-api-basic-and-free/

https://programming-zero.net/twitter-api-process/

https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api

以上より、使用していた**Standard(旧無料プラン)の機能であった他ユーザーのツイート取得が、Free(現無料プラン)では不可**ということが判明しました。

※3番目のリンクにあるTweet caps - Pull が APIのGETリクエストに該当するかと思われます。

　1,2番目のリンクにて、Freeプランにてgetリクエストを行うと、403エラー（内容は有効なkeyとtokenを使用せよ）が出力される旨が記載されています。

 　･･･実際、ターミナルにて、ファイルを実行すると同様の記載がでました。

![スクリーンショット of terminal execute serch_tweets1.py](https://images.microcms-assets.io/assets/7ac15f6666c24a5f88467fd874441472/b22c21e0c00b42ac91114c6211cd6f62/x_api%E3%81%AE%E9%96%8B%E7%99%BA%E4%B8%AD%E6%AD%A2.png)

よって、エラーの原因は「apiの有料化にまつわる騒動」と断定、また、当計画は凍結します。
