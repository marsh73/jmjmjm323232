'use strict';

angular.module('App', [
	'ngResource'
	])
	.factory('Trainers',function($resource){
		return $resource(
			'/api/trainers',
			{'query': {method: 'GET', isArray: false }}
			);
	})
	.controller('ctrlOne', function	($scope, $resource, Trainers) {
		$scope.stuffs = ['hello','goodbye','otherstuff'];
		$scope.trainers = Trainers.get();
	});
