---
layout: "post"
title: Some favorite photos
image: /img/galleries/g01/ChessBoard_THUMB.jpg
date: "2017-06-02"
tags: photography
---

<!-- Gallery __-->			
{% include subgallery1.html gal="gal1_favphotos" %}
<!-- end of GALLERY __ -->


These are some of my favorite photos that I've taken. Mostly doing this to try and get image handling slightly nicer than just directly embedding the full res jpgs. Solution so far is a mix of jquery [magnific popup](http://dimsemenov.com/plugins/magnific-popup/) and [photorama's](https://github.com/sunbliss/photorama) galleries. I've changed the "<img src" to use a liquid filter serving half-sized images within the post, magnific takes the href value for displaying the full screen image. To this end I also wrote a script for processing an gallery image files. Using [imagemagick](http://www.imagemagick.org/script/index.php) the script resizes all images to 1600 x ? for full resolution displayed, it copies and reduces these images by 30% for displaying in-line and lastly it runs [imageOptim](https://imageoptim.com/) on all images to further minimize the filesize. 


{% highlight python %}
{% include /python/image_resize.py %}
{% endhighlight %}


