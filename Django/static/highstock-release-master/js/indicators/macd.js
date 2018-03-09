/*
  Highcharts JS v6.0.3 (2017-11-14)

 Indicator series type for Highstock

 (c) 2010-2017 Sebastian Bochan

 License: www.highcharts.com/license
*/
(function(m){"object"===typeof module&&module.exports?module.exports=m:m(Highcharts)})(function(m){(function(b){var m=b.isArray;b=b.seriesType;b("ema","sma",{name:"EMA (14)",params:{index:0,period:14}},{getValues:function(b,p){var d=p.period,n=b.xData,e=b.yData,a=e?e.length:0;b=2/(d+1);var c=0,l=0,r=0,k=[],f=[],h=[],g=-1,t=[];if(n.length<d)return!1;for(m(e[0])&&(g=p.index?p.index:0);l<d;)t.push([n[l],0>g?e[l]:e[l][g]]),r+=0>g?e[l]:e[l][g],l++;p=r/d;for(d=l;d<a;d++)l=0>g?e[d-1]:e[d-1][g],c=[n[d-1],
0===c?p:l*b+c*(1-b)],k.push(c),f.push(c[0]),h.push(c[1]),c=c[1],t.push([n[d],0>g?e[d]:e[d][g]]);e=0>g?e[d-1]:e[d-1][g];c=[n[d-1],0===c?void 0:e*b+c*(1-b)];k.push(c);f.push(c[0]);h.push(c[1]);return{values:k,xData:f,yData:h}}})})(m);(function(b){var m=b.seriesType,q=b.each,p=b.merge,d=b.defined,n=b.seriesTypes.sma,e=b.seriesTypes.ema;m("macd","sma",{name:"MACD (26, 12, 9)",params:{shortPeriod:12,longPeriod:26,signalPeriod:9,period:26},signalLine:{styles:{lineWidth:1,lineColor:void 0}},macdLine:{styles:{lineWidth:1,
lineColor:void 0}},threshold:0,groupPadding:.1,pointPadding:.1,states:{hover:{halo:{size:0}}},tooltip:{pointFormat:'\x3cspan style\x3d"color:{point.color}"\x3e\u25cf\x3c/span\x3e \x3cb\x3e {series.name}\x3c/b\x3e\x3cbr/\x3eValue: {point.MACD}\x3cbr/\x3eSignal: {point.signal}\x3cbr/\x3eHistogram: {point.y}\x3cbr/\x3e'},dataGrouping:"averages",minPointLength:0},{pointArrayMap:["y","signal","MACD"],parallelArrays:["x","y","signal","MACD"],pointValKey:"y",markerAttribs:b.noop,getColumnMetrics:b.seriesTypes.column.prototype.getColumnMetrics,
crispCol:b.seriesTypes.column.prototype.crispCol,init:function(){n.prototype.init.apply(this,arguments);this.options=p({signalLine:{styles:{lineColor:this.color}},macdLine:{styles:{color:this.color}}},this.options)},toYData:function(a){return[a.y,a.signal,a.MACD]},translate:function(){var a=this,c=["plotSignal","plotMACD"];b.seriesTypes.column.prototype.translate.apply(a);q(a.points,function(b){q([b.signal,b.MACD],function(d,e){null!==d&&(b[c[e]]=a.yAxis.toPixels(d,!0))})})},destroy:function(){this.graph=
null;this.graphmacd=this.graphmacd.destroy();this.graphsignal=this.graphsignal.destroy();n.prototype.destroy.apply(this,arguments)},drawPoints:b.seriesTypes.column.prototype.drawPoints,drawGraph:function(){for(var a=this,c=a.points,b=c.length,e=a.options,k={options:{gapSize:e.gapSize}},f=[[],[]],h;b--;)h=c[b],d(h.plotMACD)&&f[0].push({plotX:h.plotX,plotY:h.plotMACD,isNull:!d(h.plotMACD)}),d(h.plotSignal)&&f[1].push({plotX:h.plotX,plotY:h.plotSignal,isNull:!d(h.plotMACD)});q(["macd","signal"],function(c,
b){a.points=f[b];a.options=p(e[c+"Line"].styles,k);a.graph=a["graph"+c];n.prototype.drawGraph.call(a);a["graph"+c]=a.graph});a.points=c;a.options=e},getValues:function(a,c){var b=0,d,k,f=[],h=[],g=[];d=e.prototype.getValues(a,{period:c.shortPeriod});k=e.prototype.getValues(a,{period:c.longPeriod});d=d.values;k=k.values;for(a=1;a<=d.length;a++)k[a-1]&&k[a-1][1]&&f.push([d[a+c.shortPeriod+1][0],0,null,d[a+c.shortPeriod+1][1]-k[a-1][1]]);for(a=0;a<f.length;a++)h.push(f[a][0]),g.push([0,null,f[a][3]]);
c=e.prototype.getValues({xData:h,yData:g},{period:c.signalPeriod,index:2});c=c.values;for(a=0;a<f.length;a++)f[a][0]>=c[0][0]&&(f[a][2]=c[b][1],g[a]=[0,c[b][1],f[a][3]],null===f[a][3]?(f[a][1]=0,g[a][0]=0):(f[a][1]=f[a][3]-c[b][1],g[a][0]=f[a][3]-c[b][1]),b++);return{values:f,xData:h,yData:g}}})})(m)});
