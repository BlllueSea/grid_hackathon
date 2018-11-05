        $(function(){
           var nutrition = ["calories",
                            "carbohydrate",
                            "proteins",
                            "fat",
                            "dietary_fiber",
                            "sodium",
                            "sodium_chloride_equivalent",
                            "potassium",
                            "calcium",
                            "iron",
                            "magnesium",
                            "phosphorus",
                            "vitamin_A",
                            "vitamin_B1",
                            "vitamin_B2",
                            "vitamin_B6",
                            "vitamin_B12",
                            "niacin",
                            "vitamin_C",
                            "vitamin_D",
                            "vitamin_E"];


   // Handle drag and drop events with jQuery
          var obj = $("#dragandrophandler");
          obj.on('dragenter', function (e)
          {
              e.stopPropagation();
              e.preventDefault();
              $(this).css('border', '2px solid #0B85A1');
          });
          obj.on('dragover', function (e)
          {
               e.stopPropagation();
               e.preventDefault();
          });
          obj.on('drop', function (e)
          {
               console.log('test');

               $(this).css('border', '2px dotted #0B85A1');
               e.preventDefault();

               // ドラッグドロップされたファイルのオブジェクト
               var files = e.originalEvent.dataTransfer.files;
               console.log(files);

               showFileContents(files,obj);
          });



   // prevent ‘drop’ event on other place of the browser window
         $(document).on('dragenter', function (e)
         {
             e.stopPropagation();
             e.preventDefault();
         });
         $(document).on('dragover', function (e)
         {
           e.stopPropagation();
           e.preventDefault();
           obj.css('border', '2px dotted #0B85A1');
         });
         $(document).on('drop', function (e)
         {
             e.stopPropagation();
             e.preventDefault();
         });



   // Read the file contents using HTML5 FormData() when the files are dropped.
         function showFileContents(files,obj)
         {
            var s='';

            for (var i = 0; i < files.length; i++){
                 var formData = new FormData();
                 formData.append('file', files[i]);
                 s += '<div>file name : ' + files[i].name + '</div>';
                 sendFileToServer(formData);
            }
//            console.log(fd.length)

           $('#showFileName').html(s);
         }


         function getSexForFormData(formData){
            var sex = document.querySelector('input[name="sex"]:checked').value;
            // check sex-> alert(sex+ ' was selected!');
            formData.append('sex',sex);
            return formData;
      }

         //送信
         function sendFileToServer(formData){
           $('#submitBtn').on('click', function(e){ //送信ボタンが押されたら
                 e.preventDefault();
                 formData = getSexForFormData(formData);
                 console.log(formData);

                 // サーバーに送る　→　サーバーからの出力表示
//                 var path = 'http://localhost:8080/upload/' + fName;
//                 console.log(path);

                 $.ajax({
                     method: 'post',
                     url: '/upload',　//(ここには処理系を書く(ふつうはphpだけど、今回はpython))
                     dataType: 'json',
                     data: formData, //　送る画像のパス
                     processData: false,
                     contentType: false

                 }).done(function (res) {
                     console.log('done');
                     var percent = res.per_dict// 成功した場合、レスポンスからデータを取り出します。
                     var real_value = res.real_value
                     console.log(res.food_name)

                     var bargraph_color = ['#000000',
                         '#808080',
                         '#C0C0C0C0',
                         '#CCFFFF',
                         '#0000ff',
                         '#00FFFF',
                         '#008000',
                         '#00ff00',
                         '#FFFF00',
                         '#800080',
                         '#ff00ff',
                         '#FF0000',
                         '#98fb98',
                         '#90ee90',
                         '#adff2f',
                         '#7fff00',
                         '#7cfc00',
                         '#00ff7f',
                         '#00fa9a',
                         '#7fffd4',
                         '#40e0d0'
                       ];

                     new Chart(document.getElementById("myChart_1"), { //横にしているから軸は逆
                         type: "horizontalBar",
                         data: {
                           labels: nutrition,
                           datasets: [{
                             data: [percent.calories,
                                    percent.carbohydrate,
                                    percent.proteins,
                                    percent.fat,
                                    percent.dietary_fiber,
                                    percent.sodium,
                                    percent.sodium_chloride_equivalent,
                                    percent.potassium,
                                    percent.calcium,
                                    percent.iron,
                                    percent.magnesium,
                                    percent.phosphorus,
                                    percent.vitamin_A,
                                    percent.vitamin_B1,
                                    percent.vitamin_B2,
                                    percent.vitamin_B6,
                                    percent.vitamin_B12,
                                    percent.niacin,
                                    percent.vitamin_C,
                                    percent.vitamin_D,
                                    percent.vitamin_E
                                  ],
                             backgroundColor: bargraph_color
                           }]
                         },
                         options:{
                           responsive: false,
                           legend: {
                             display: false
                           },
                           title: {                         //タイトル設定
                             display: true,                 //表示設定
                             fontSize: 15,                  //フォントサイズ
                             text: 'ALL NUTRITION'                //ラベル
                           },
                           scales:{
                             yAxes:[{
                               display: true,                //表示設定
                               barPercentage: 0.7,           //棒グラフ幅
                               categoryPercentage: 0.5,      //棒グラフ幅
                               scaleLabel: {                 //軸ラベル設定
                                 display:false,             //表示設定
                                 labelString: '',  //ラベル
                                 fontSize: 11
                               }              //フォントサイズ
                             }],
                             xAxes: [{
                               display: true,
                               ticks: { //軸設定
                                 min: 0,
                                 max: 120,
                                 fontSize: 11,
                                 stepSize: 5
                               }
                             }]
                            }
                          }
                     });

                     new Chart(document.getElementById("myChart_2"), {
                         type: 'radar',
                         data: {
                            labels: ["protains", "salt", "energe", "lipid", "carbohydrate", "iron", "vitaminC"],
                            datasets: [{
                              label: 'Main Nutrition',
                              borderColor: "#ccffcc",
                              borderColor: "#00FF00",
                              data: [percent.proteins, percent.sodium_chloride_equivalent, percent.calories, percent.fat, percent.carbohydrate, percent.iron, percent.vitamin_C]
                            },{
                              label: 'Reference Value',
                              borderColor: "#C0C0C0",
                              data: [100, 100, 100, 100, 100, 100, 100]
                            }],
                         options:{
                           responsive: false,
                           legend: {
                             display: true
                           },
                           title: {
                             display: true,
                             fontSize: 15,
                             text: 'MAIN NUTRITION'
                           },
                           scale: {
                             display: true,
                             pointLabels: {
                              fontSize: 11,
                             },
                             ticks: {
                              display: true,
                              fontSize: 9,
                              fontColor: "#000000",
                                min: 0,
                                max: 120,
                                beginAtZero: true
                            }
                           }
                          }
                       }
                     });


                     $("#result").append()
                     $("#food").html( "<b>"+ res.food_name +"</b>, aren't you?");

                   	 $("#out1").html('<div class="siimple-table-cell">calories </div><div class="siimple-table-cell">'+ real_value.calories +' kcal</div>');
                   	 $("#out2").html('<div class="siimple-table-cell">carbohydrate </div><div class="siimple-table-cell">'+ real_value.carbohydrate +' g</div>');
                   	 $("#out3").html('<div class="siimple-table-cell">proteins </div><div class="siimple-table-cell">'+ real_value.proteins +' g</div>');
                   	 $("#out4").html('<div class="siimple-table-cell">fat </div><div class="siimple-table-cell">'+ real_value.fat +' g</div>');
                     $("#out5").html('<div class="siimple-table-cell">dietary_fiber </div><div class="siimple-table-cell">'+ real_value.dietary_fiber +' g</div>');
                     $("#out6").html('<div class="siimple-table-cell">sodium </div><div class="siimple-table-cell">'+ real_value.sodium +' mg</div>');
                     $("#out7").html('<div class="siimple-table-cell">sodium_chloride_equivalent </div><div class="siimple-table-cell">'+ real_value.sodium_chloride_equivalent +' g</div>');
                     $("#out8").html('<div class="siimple-table-cell">potassium </div><div class="siimple-table-cell">'+ real_value.potassium +' mg</div>');
                     $("#out9").html('<div class="siimple-table-cell">calcium </div><div class="siimple-table-cell">'+ real_value.calcium +' mg</div>');
                     $("#out10").html('<div class="siimple-table-cell">iron </div><div class="siimple-table-cell">'+ real_value.iron +' mg</div>');
                     $("#out11").html('<div class="siimple-table-cell">magnesium </div><div class="siimple-table-cell">'+ real_value.magnesium +' mg</div>');
                     $("#out12").html('<div class="siimple-table-cell">phosphorus </div><div class="siimple-table-cell">'+ real_value.phosphorus +' mg</div>');
                     $("#out13").html('<div class="siimple-table-cell">vitamin_A </div><div class="siimple-table-cell">'+ real_value.vitamin_A +' μg</div>');
                     $("#out14").html('<div class="siimple-table-cell">vitamin_B1 </div><div class="siimple-table-cell">'+ real_value.vitamin_B1 +' mg</div>');
                     $("#out15").html('<div class="siimple-table-cell">vitamin_B2 </div><div class="siimple-table-cell">'+ real_value.vitamin_B2 +' mg</div>');
                     $("#out16").html('<div class="siimple-table-cell">vitamin_B6 </div><div class="siimple-table-cell">'+ real_value.vitamin_B6 +' mg</div>');
                     $("#out17").html('<div class="siimple-table-cell">vitamin_B12 </div><div class="siimple-table-cell">'+ real_value.vitamin_B12 +' μg</div>');
                     $("#out18").html('<div class="siimple-table-cell">niacin </div><div class="siimple-table-cell">'+ real_value.niacin +' mg</div>');
                     $("#out19").html('<div class="siimple-table-cell">vitamin_C </div><div class="siimple-table-cell">'+ real_value.vitamin_C +' mg</div>');
                     $("#out20").html('<div class="siimple-table-cell">vitamin_D </div><div class="siimple-table-cell">'+ real_value.vitamin_D +' μg</div>');
                     $("#out21").html('<div class="siimple-table-cell">vitamin_E </div><div class="siimple-table-cell">'+ real_value.vitamin_E +' mg</div>');

                     $("#radar_chart").append('<img src='+res.radar_chart_path+' alt="radar chart">');

                     $("#recommend_menu").append("<b>"+res.recommend_menu+"</b>");
                     $("#recommend_img").append('<div class="card-body-content"><img src='+res.recommend_img_path+' alt="recommend"></div>');


                 }).fail(function(data) {
                     console.log('fail')
                 })
               });
         }
     });
