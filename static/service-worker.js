importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');

/*
workbox.routing.registerRoute(
	({request}) => reguest.destination === "image",
	new workbox.strategies.CacheFirst()
);

console.log('Service Worker');*/


// cache name
workbox.core.setCacheNameDetails({
    prefix: 'chona-cache',
    precache: 'precache',
    runtime: 'runtime',
  });
  
// runtime cache

workbox.routing.registerRoute(
    new RegExp('/static/.*'),
    new workbox.strategies.CacheFirst({
			cacheName: 'chona-cache-Static'
		})
);

// 1. stylesheet
workbox.routing.registerRoute(
    new RegExp('\.css$'),
    new workbox.strategies.CacheFirst({
        cacheName: 'chona-cache-Stylesheets'
    })
);
// 2. images
workbox.routing.registerRoute(
    new RegExp('\.(png|svg|jpg|jpeg)$'),
    new workbox.strategies.CacheFirst({
        cacheName: 'chona-cache-Images'
    })
);
workbox.routing.registerRoute(
    new RegExp('/.*'),
    new workbox.strategies.CacheFirst()
);


workbox.precaching.precacheAndRoute([]);