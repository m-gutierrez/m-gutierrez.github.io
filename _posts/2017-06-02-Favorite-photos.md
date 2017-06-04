---
layout: "post"
title: Some favorite photos
image: /img/galleries/g01/ChessBoard_THUMB.jpg
date: "2017-06-02"
---

<!-- Gallery __-->			
{% include subgallery.html gal="gal1_favphotos" %}
<!-- end of GALLERY __ -->


These are some of my favorite photos that I've taken. Mostly doing this to try and get image handling slightly nicer than just directly embedding the full res jpgs. Solution so far is a mix of jquery [magnific popup](http://dimsemenov.com/plugins/magnific-popup/) and [photorama's](https://github.com/sunbliss/photorama) galleries. I've changed the "<img src" to use a liquid filter serving half-sized images within the post, magnific takes the href