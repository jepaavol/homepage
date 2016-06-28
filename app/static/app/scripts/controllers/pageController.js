//Page Module
var pageApp = angular.module('page', ['ngSanitize', 'duScroll']);

pageApp.controller('PageController', function PageController($scope, $http, $log, $timeout) {
    $http.get("/api/page/2")
    .then(function (response) {
        //API Succesfully called
        $scope.page = response.data;
        $scope.log = $log;
        $scope.naviItems = [];

        //Logic to get items in separate variable that needs to be presented in navibar
        for (index = 0, len = $scope.page.sections.length; index < len; index++) {
            var navisectiontypes = ['textSection', 'iconSection'];
            if (navisectiontypes.indexOf($scope.page.sections[index].type) != -1) {
                $scope.naviItems.push($scope.page.sections[index]);
                $scope.page.sections[index].showHeader = true;
            }
        }
        $scope.naviItems = _.sortBy($scope.naviItems, 'order');

        //Ordering sections
        $scope.sections = _.sortBy($scope.page.sections, 'order');

    }, function (response) {
        $scope.error = "API call failed: " + response.status + " " + response.statustext;
    });
});