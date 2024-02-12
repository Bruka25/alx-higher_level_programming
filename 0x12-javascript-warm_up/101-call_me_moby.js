#!/usr/bin/node
exports.callMeMoby = function (times, theFunction) {
  for (let i = 0; i < times; i++) theFunction();
};
