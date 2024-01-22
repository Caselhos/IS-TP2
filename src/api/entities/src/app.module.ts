import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import {AlbumsModule} from "./albums/albums.module";
import {ArtistsModule} from "./artists/artists.module";
import {MusicsModule} from "./musics/musics.module";
import {CountriesModule} from "./countries/countries.module";

@Module({
  imports: [AlbumsModule, ArtistsModule, MusicsModule,CountriesModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
